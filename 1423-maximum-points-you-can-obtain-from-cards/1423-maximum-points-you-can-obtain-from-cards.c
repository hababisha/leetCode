int maxScore(int* cardPoints, int cardPointsSize, int k) {
    int lsum = 0, rsum = 0;
    int maxsum = 0;
    int i;

    for (i = 0; i < k; i++) {
        lsum += cardPoints[i];
    }

    maxsum = lsum;

    for (i = 0; i < k; i++) {
        lsum -= cardPoints[k - 1 - i];          
        rsum += cardPoints[cardPointsSize - 1 - i];   
        maxsum = fmax(maxsum, lsum + rsum);
    }

    return maxsum;
}
