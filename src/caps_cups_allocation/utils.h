

#ifndef UTILS_H
#define UTILS_H

#include <bits/stdc++.h>
#include <pthread.h>
#include <thread>
#include <random>
using namespace std;



vector<pair<int, int>> random_points_generator(int size);
int orientation(pair<int, int> p1, pair<int, int> p2, pair<int, int> p3);
void finding_covex_caps(vector<pair<int, int>> cands, vector<pair<int, int>> &points,
                        unordered_map<string, vector<pair<int, int>>>& caps, set<pair<int, int>>& seen);
unordered_map<string, vector<pair<int, int>>> all_convex(vector<pair<int, int> > points);
#endif //UTILS_H
