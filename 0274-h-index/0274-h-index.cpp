class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = static_cast<int>(citations.size());
        std::vector<int> buckets(n + 1, 0);

        // Count papers by capped citation count
        for (int c : citations) {
            if (c >= n) buckets[n]++;   // overflow bucket
            else        buckets[c]++;
        }

        // Accumulate from high to low to find largest h with count >= h
        int count = 0;
        for (int h = n; h >= 0; --h) {
            count += buckets[h];
            if (count >= h) return h;
        }
        return 0; // fallback, though loop will return before this
    }
};