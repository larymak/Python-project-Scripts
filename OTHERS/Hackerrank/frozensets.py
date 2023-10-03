set1 = {'A','B','C','D'}
set2 = {'A',2,'C',4}
frozen_set_1 = frozenset(set1)
frozen_set_2 = frozenset(set2)

frozenset_union = frozen_set_1.union(frozen_set_2)
frozenset_common = frozen_set_1.intersection(frozen_set_2)
frozenset_difference = frozen_set_1.difference(frozen_set_2)
frozenset_distinct = frozen_set_1.symmetric_difference(frozen_set_2)

print("frozen_set_1:",frozen_set_1)
print("frozen_set_2:",frozen_set_2)
print("frozenset_union:",frozenset_union)
print("frozenset_common:",frozenset_common)
print("frozenset_difference:",frozenset_difference)
print("frozenset_distinct:",frozenset_distinct)