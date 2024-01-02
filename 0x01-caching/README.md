# Caching

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- **What a caching system is:**
  A caching system is a mechanism used to store and retrieve data quickly by keeping a copy of frequently accessed information in a temporary storage space, often faster than the original data source.

- **What FIFO means:**
  FIFO stands for "First In, First Out." It is a caching policy where the oldest item that wassite of LRU, where the most recently accessed item is the one retained in the cache when the cache is full.

- **What LFU means:**
  LFU stands for "Least Frequently Used." This caching strategy removes the least frequently accessed item when the cache bec added to the cache is the first one to be removed when the cache reaches its limit.

- **What LIFO means:**
  LIFO stands for "Last In, First Out." In this caching policy, the most recently added item is the first one to be removed when the cache is full.

- **What LRU means:**
  LRU stands for "Least Recently Used." It is a caching strategy that removes the least recently accessed item from the cache when its capacity is reached.

- **What MRU means:**
  MRU stands for "Most Recently Used." It is the oppoomes full.

- **What the purpose of a caching system is:**
  The purpose of a caching system is to improve data access speed by storing frequently accessed information in a cache, reducing the need to fetch it from the original data source repeatedly.

- **What limits a caching system has:**
  Caching systems have limitations such as:
  - **Capacity Limitation:** Caches have a finite capacity, and once that limit is reached, older or less frequently accessed items must be removed to make space for new data.
  - **Consistency Challenges:** Caches may introduce data consistency challenges, as the cached data might become outdated compared to the original source.
  - **Complexity and Overhead:** Implementing and managing caching systems can introduce complexity and overhead in terms of maintenance and synchronization with the original data source.

**Examples:**

Consider a simple web application that retrieves user profiles from a database. To speed up access, a caching system can be implemented.

- **FIFO Example:**
  If the cache has a limit of 100 entries and user profiles are fetched frequently, the oldest profile (first in) would be removed when the cache is full.

- **LRU Example:**
  If user profiles are accessed at varying frequencies, the least recently accessed profile would be evicted from the cache when the limit is reached.

- **LFU Example:**
  In a scenario where some user profiles are accessed more frequently than others, the least frequently accessed profile would be removed from the cache.

- **Capacity Limitation Example:**
  If the cache can only store 100 profiles, attempting to cache more than that would result in eviction of older entries.

- **Consistency Challenges Example:**
  If a user updates their profile in the database, the cache might still contain the outdated information until it is refreshed.

- **Complexity and Overhead Example:**
  Implementing cache eviction policies, cache synchronization, and dealing with cache invalidation can introduce additional complexity and maintenance overhead.
