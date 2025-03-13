//
// Created by abanoubaziz on 3/12/25.
//

// In this Module, we are working on making all the needed functions

#include "utils.h"

/**
 * random_point_generator - generating the random points, ensureing that there are no more than 3 point colinear
 * @param size
 * @return array of points
 */
vector<pair<int, int>> random_points_generator(int size) {

    // Ensuring that a value never been repeated, nor there are more than three points in colinear position
    unordered_map<int, set<int>> seen;
    vector<int> x_axis(100 + 1, 0);
    vector<int> y_axis(100 + 1, 0);
    vector<pair<int, int>> points;

    // Configureing Random Generator
    // TODO: Make a smarter way to generate points for better results
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dist(0, 100);

    while (points.size() < size) {
        int x = dist(gen);
        int y = dist(gen);
        if (x_axis[x] < 1 and y_axis[y] < 1 and seen[x].find(y) == seen[x].end()) {
            points.push_back(make_pair(x, y));
            seen[x].insert(y);
            x_axis[x]++;
            y_axis[y]++;
        }
    }

    sort(points.begin(), points.end(), [](const pair<int, int>& p1, const pair<int, int>& p2) {
        if (p1.first != p2.first) {
            return p1.first < p2.first;
        }
        return p1.second < p2.second;
    });
    return points;
}


/**
 * orientation - finding the orientation of the points in space
 * @param p1 point 1
 * @param p2 point 2
 * @param p3 point 3
 * @return -1 when counterclockwise, 0 when colinear, 1 when clockwise
 */
int orientation(pair<int, int> p1, pair<int, int> p2, pair<int, int> p3) {
    int orien = (p2.second - p1.second) * (p3.first - p2.first) -
        (p2.first - p1.first) * (p3.second - p2.second);

    if (orien == 0) return orien;
    else return (orien > 0) ? 1 : -1;
}

void print_arr(vector<pair<int, int>> vals, string handle) {
    cout << "Convex-shape: " << handle << endl;
    for (auto val : vals) {
        cout << "(" << val.first << ", " << val.second << "),";
    }
    cout << endl;
}


/**
 * fiding_covex_caps - generating all the caps of found in this orientation
 * @param cands - candidates values for a convex cap
 * @param points - points of the whole sample space
 * @param caps - recorded values of caps
 * return none;
 */
void finding_covex_caps(vector<pair<int, int>> cands, vector<pair<int, int>>& points,
                        unordered_map<string, vector<pair<int, int>>>& caps, set<pair<int, int>>& seen) {
    if (cands.size() < 2) {
        return;
    }

    int csize = cands.size();
    int left = 0, right = points.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (points[mid].first < cands[csize - 1].first) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }

    if (left >= points.size()) {
        return;
    }

    for (int i = left; i < points.size(); i++) {
        // Check orientation without modification
        if (orientation(cands[csize - 2], cands[csize - 1], points[i]) != -1) {
            // Check if point is already seen
            if (seen.find(points[i]) != seen.end() and points[i].first >= cands[csize - 1].first) continue;

            cands.push_back(points[i]);
            vector<pair<int, int>> snapshot(cands);

            // Construct handle for the map
            string handle = to_string(cands[0].first) + "," + to_string(cands[0].second) + "-"
                          + to_string(points[i].first) + "," + to_string(points[i].second);

            caps[handle] = snapshot;
            print_arr(cands, handle);


            // Mark the point as seen
            seen.insert(points[i]);

            // Recurse to find more convex caps
            finding_covex_caps(cands, points, caps, seen);

            // Backtrack: remove the last point and mark it as not seen
            cands.pop_back();
            seen.erase(points[i]);
        }
    }
}

unordered_map<string, vector<pair<int, int>>> all_convex(vector<pair<int, int>> points) {
    unordered_map<string, vector<pair<int, int>>> caps;
    set<pair<int, int>> seen;
    vector<pair<int, int>> cands;


    cands.push_back(points[0]);
    seen.insert(points[0]);

    for (int i = 1; i < points.size(); i++) {
        cands.push_back(points[i]);
        seen.insert(points[i]);
        finding_covex_caps(cands, points, caps, seen);
        seen.erase(points[i]);
        cands.pop_back();
    }

    return caps;
}