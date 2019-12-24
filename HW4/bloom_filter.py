# TODO: Your name, Cornell NetID
# TODO: Your Partner's name, Cornell NetID

# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1
from cs5112_hash import cs5112_hash2
from cs5112_hash import cs5112_hash3

# Implementation of a basic bloom filter. Uses exactly three hash functions.
class BloomFilter:
  def __init__(self, size=10):
    # DO NOT EDIT THIS CONSTRUCTOR
    self.size = size
    self.array = FixedSizeArray(size)
    for i in range(0, size):
      self.array.set(i, False)

  # To add an element to the bloom filter, use each of the k=3 hash functions we provided and compute
  # the positions that we are setting in the fixed size array using modulo operation.
  def add_elem(self, elem):
    #TODO: YOUR CODE HERE, delete the line below and implement accordingly
    hash_1 = cs5112_hash1(elem)
    hash_1_res_rightmost = hash_1 % self.size
    self.array.set(hash_1_res_rightmost, True)

    hash_2 = cs5112_hash2(elem)
    hash_2_res_rightmost = hash_2 % self.size
    self.array.set(hash_2_res_rightmost, True)

    hash_3 = cs5112_hash3(elem)
    hash_3_res_rightmost = hash_3 % self.size
    self.array.set(hash_3_res_rightmost, True)

    #hash_res = cs5112_hash3(cs5112_hash2(cs5112_hash1(elem)))
    #hash_res_rightmost = hash_res % 10
    
    # while (hash_res > 0):
    #   hash_res_rightmost = hash_res % 10
    #   self.array.set(hash_res_rightmost, True)
    #   hash_res = hash_res / 10

  # Returns False if the given element was definitely not added to the filter. 
  # Returns True if it's possible that the element was added to the filter.
  def check_membership(self, elem):
    #TODO: YOUR CODE HERE, delete the line below and implement accordingly
    hash_1 = cs5112_hash1(elem)
    hash_1_res_rightmost = hash_1 % self.size
    bool1 = self.array.get(hash_1_res_rightmost)

    hash_2 = cs5112_hash2(elem)
    hash_2_res_rightmost = hash_2 % self.size
    bool2 = self.array.get(hash_2_res_rightmost)

    hash_3 = cs5112_hash3(elem)
    hash_3_res_rightmost = hash_3 % self.size
    bool3 = self.array.get(hash_3_res_rightmost)

    if (bool1 and bool2 and bool3):
      return True

    return False
