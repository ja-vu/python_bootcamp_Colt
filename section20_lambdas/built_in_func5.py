# zip
# make an iterator that aggregates elements from each of the iterables
# Returns an iterator of tuples, where the ith tuple contains the i-th element from each of the argument
# sequences or iterables.
# The iterator stops when the shortest input iterable is exhausted

first_zip = zip([1,2,3],[4,5,6])
list(first_zip) # [(1,4), (2,5), (3,6)

midterms = [80,91,78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

# We want the results to show like this:
# final_grades = {'dan':98, "ang":91....}


# dict comprehension method

# final_grades = [max(pair) for pair in zip(midterms, finals)]
final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
print(final_grades)

# map
scores = \
dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms,finals)
        )
    )
)

print(scores)


# another tweak

avg_grades = \
dict(
    zip(
        students,
        map(
            lambda pair:((pair[0]+pair[1])/2),
            zip(midterms,finals)
        )
    )
)

print(avg_grades)
