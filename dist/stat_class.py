# See the file LICENSE for redistribution information.
#
# Copyright (c) 2008 WiredTiger Software.
#	All rights reserved.
#
# $Id$
#
# Auto-generate statistics #defines, with allocation, clear and print functions.
#
# The XXX_stats dictionaries are a set of objects consisting of comma-separated
# configuration key words and a text description.  The configuration key words
# are:
#	perm	-- Field is not cleared by the stat clear function.

class Stat:
	def __init__(self, config, str):
		self.config = config
		self.str = str

##########################################
# IENV handle statistics
##########################################
ienv_stats = {}
ienv_stats['DATABASE_OPEN'] = Stat([], 'database open')
ienv_stats['MEMALLOC'] = Stat([], 'memory allocations')
ienv_stats['MEMFREE'] = Stat([], 'memory frees')
ienv_stats['MTX_LOCK'] = Stat([], 'mutex lock calls')
ienv_stats['TOTAL_READ_IO'] = Stat([], 'total read I/Os')
ienv_stats['TOTAL_WRITE_IO'] = Stat([], 'total write I/Os')
ienv_stats['WORKQ_PASSES'] = Stat([], 'workQ queue passes')
ienv_stats['WORKQ_SLEEP'] = Stat([], 'workQ sleeps')
ienv_stats['WORKQ_YIELD'] = Stat([], 'workQ yields')

##########################################
# Cache handle statistics
##########################################
cache_stats = {}
cache_stats['CACHE_ALLOC'] = Stat([], 'pages allocated in the cache')
cache_stats['CACHE_BYTES_INUSE'] = Stat(['perm'], 'bytes in the cache')
cache_stats['CACHE_BYTES_MAX'] = Stat(['perm'], 'maximum bytes configured for the cache')
cache_stats['CACHE_EVICT'] = Stat([], 'unmodified pages evicted from the cache')
cache_stats['CACHE_EVICT_HAZARD'] = Stat([], 'pages not evicted because of a hazard reference')
cache_stats['CACHE_EVICT_MODIFIED'] = Stat([], 'modified pages evicted from the cache')
cache_stats['CACHE_HASH_BUCKETS'] = Stat([], 'hash buckets')
cache_stats['CACHE_HIT'] = Stat([], 'reads found in the cache')
cache_stats['CACHE_MAX_BUCKET_ENTRIES'] = Stat([], 'maximum entries allocated to a hash bucket')
cache_stats['CACHE_MISS'] = Stat([], 'reads not found in the cache')
cache_stats['CACHE_PAGES_INUSE'] = Stat(['perm'], 'pages in the cache')
cache_stats['CACHE_READ_LOCKOUT'] = Stat([], 'API cache read lockout')
cache_stats['CACHE_READ_RESTARTS'] = Stat([], 'cache read restarts')

##########################################
# IDB handle statistics
##########################################
idb_stats = {}
idb_stats['BULK_DUP_DATA_READ'] = Stat([], 'bulk duplicate data pairs read')
idb_stats['BULK_HUFFMAN_DATA'] = Stat([], 'bulk insert huffman data compression')
idb_stats['BULK_HUFFMAN_KEY'] = Stat([], 'bulk insert huffman key compression')
idb_stats['BULK_OVERFLOW_DATA'] = Stat([], 'bulk overflow data items read')
idb_stats['BULK_OVERFLOW_KEY'] = Stat([], 'bulk overflow key items read')
idb_stats['BULK_PAIRS_READ'] = Stat([], 'bulk key/data pairs inserted')
idb_stats['BULK_REPEAT_COUNT'] = Stat([], 'bulk insert repeat count compression')
idb_stats['DB_CACHE_ALLOC'] = Stat([], 'pages allocated in the cache')
idb_stats['DB_CACHE_HIT'] = Stat([], 'cache hit: reads found in the cache')
idb_stats['DB_CACHE_MISS'] = Stat([], 'cache miss: reads not found in the cache')

##########################################
# IDB database statistics
##########################################
idb_dstats = {}
idb_dstats['BASE_RECNO'] = Stat([], 'base record number')
idb_dstats['FIXED_LEN'] = Stat([], 'database fixed-record size')
idb_dstats['INTLMAX'] = Stat([], 'maximum internal page size')
idb_dstats['INTLMIN'] = Stat([], 'minimum internal page size')
idb_dstats['ITEM_DATA_OVFL'] = Stat([], 'overflow data items')
idb_dstats['ITEM_DUP_DATA'] = Stat([], 'duplicate data items')
idb_dstats['ITEM_KEY_OVFL'] = Stat([], 'overflow keys')
idb_dstats['ITEM_TOTAL_DATA'] = Stat([], 'total database data items')
idb_dstats['ITEM_TOTAL_KEY'] = Stat([], 'total database keys')
idb_dstats['LEAFMAX'] = Stat([], 'maximum leaf page size')
idb_dstats['LEAFMIN'] = Stat([], 'minimum leaf page size')
idb_dstats['MAGIC'] = Stat([], 'magic number')
idb_dstats['MAJOR'] = Stat([], 'major version number')
idb_dstats['MINOR'] = Stat([], 'minor version number')
idb_dstats['PAGE_COL_FIXED'] = Stat([], 'column-store fixed-size leaf pages')
idb_dstats['PAGE_COL_INTERNAL'] = Stat([], 'column-store internal pages')
idb_dstats['PAGE_COL_VARIABLE'] = Stat([], 'column-store variable-size leaf pages')
idb_dstats['PAGE_DUP_INTERNAL'] = Stat([], 'duplicate internal pages')
idb_dstats['PAGE_DUP_LEAF'] = Stat([], 'duplicate leaf pages')
idb_dstats['PAGE_FREE'] = Stat([], 'unused on-page space in bytes')
idb_dstats['PAGE_INTERNAL'] = Stat([], 'row-store internal pages')
idb_dstats['PAGE_LEAF'] = Stat([], 'row-store leaf pages')
idb_dstats['PAGE_OVERFLOW'] = Stat([], 'overflow pages')
idb_dstats['TREE_LEVEL'] = Stat([], 'number of levels in the Btree')

##########################################
# FH handle statistics
##########################################
fh_stats = {}
fh_stats['FSYNC'] = Stat([], 'fsyncs')
fh_stats['READ_IO'] = Stat([], 'read I/Os')
fh_stats['WRITE_IO'] = Stat([], 'write I/Os')
