class Solution {
    // private int helper(int[] cost, int[] dp, int n){
    //     // if (n == 0 ||  n == 1){
    //     //     return Math.min(cost[0], cost[1]);
    //     // }
    //     // dp[0]=cost[0];
    //     // dp[1]=cost[1];
    //     // if (dp[n] != -1){
    //     //     return dp[n];
    //     // }
    //     // dp[n] =cost[n]+ Math.min(helper(cost, dp, n - 1), helper(cost, dp, n - 2));
    //     // return dp[n];
    // }
    public int minCostClimbingStairs(int[] cost) {
        // int n = cost.length;
        // int[] dp = new int[cost.length + 1];
        // Arrays.fill(dp, -1);
        // return Math.min(helper(cost, dp, n - 1), helper(cost, dp, n - 2));
        int a = cost[0];
        int b = cost[1]; 
        for (int i = 2; i < cost.length; i++){
            int c = cost[i] + Math.min(a, b);
            a = b;
            b = c;
        }
        return Math.min(a, b);
    }
}