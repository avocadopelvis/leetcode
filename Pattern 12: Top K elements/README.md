Any problem that asks us to find the top/smallest/frequent ‘K’ elements among a given set falls under this pattern.
<br>
<br>
The best data structure to keep track of ‘K’ elements is Heap. This pattern will make use of the Heap to solve multiple problems dealing with ‘K’ elements at a time from a set of given elements. The pattern looks like this:
- Insert ‘K’ elements into the min-heap or max-heap based on the problem.
- Iterate through the remaining numbers and if you find one that is larger than what you have in the heap, then remove that number and insert the larger one.

![delete](https://user-images.githubusercontent.com/92647313/180679280-094e8582-7885-444a-a819-3d179f1b527b.jpg)

There is no need for a sorting algorithm because the heap will keep track of the elements for you.
<br>
<br>
How to identify the Top ‘K’ Elements pattern:
- If you’re asked to find the top/smallest/frequent ‘K’ elements of a given set
- If you’re asked to sort an array to find an exact element

Problems featuring Top ‘K’ Elements pattern:
- Top ‘K’ Numbers (easy)
- Top ‘K’ Frequent Numbers (medium)
