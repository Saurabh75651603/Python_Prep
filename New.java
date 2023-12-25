// import java.util.*;

// class new{
//     static class HashMap<K, V>{
//         private class Node{
//             K key;
//             V value;

//             public Node(K key, V value) {
//                 this.key = key;
//                 this.value = value;
//             }
//         }

//         private int n; //n - nodes
//         private int N; //N - buckets
//         private LinkedList<Node> buckets[]; // N = buckets.length

//         @SuppressWarnings("unchecked");


//     }

// }


public class New {
	
	public static void main(String[] args){
		
		int nums[] = {4,1,5,5,3,2};
		int target = 11;
		
		int result = linearSearch(nums, target);
		
		System.out.println("Element found at index:" + result);
		
		public static int linearSearch(int[] nums, int target){
			return -1;
			
			
		}
		
		
	}
}


public class New {

    public static void main(String[] args) {

        int nums[] = {4, 1, 5, 5, 3, 2};
        int target = 11;

        int result = linearSearch(nums, target);

        if (result != -1) {
            System.out.println("Element found at index: " + result);
        } else {
            System.out.println("Element not found in the array.");
        }
    }

    public static int linearSearch(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                return i; // Element found, return its index
            }
        }
        return -1; // Element not found in the array
    }
}
