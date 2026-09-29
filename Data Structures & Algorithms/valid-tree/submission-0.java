class Solution {
    private Map<Integer, List<Integer>> adj = new HashMap<>();

    public boolean validTree(int n, int[][] edges) {
        if (n == 1) return edges.length == 0;
        if (edges.length == 0) return false; 

        makeMap(edges, n);
        boolean[] vis = new boolean[n];

        if (!dfs(edges[0][1], -1, vis)) return false;
        
        for (int i = 0; i < n; i++) {
            if (!vis[i]) return false;
        }
        return true;
    }

    private boolean dfs(int node, int prev, boolean[] vis) {
        if (vis[node]) return false;
        
        vis[node] = true;

        for (int nbr : adj.get(node)) {
            if (nbr == prev) continue;
            if (!dfs(nbr, node, vis)) return false;
        }

        return true;
    }


    private void makeMap(int[][] edges, int n) {
        for (int i = 0; i < n; i++) adj.put(i, new ArrayList<>());
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }
    }
}
