#include "utils.h"
using namespace std;

int main() {
    vector<pair<int, int>> values = random_points_generator(33);
    for (int i = 0; i < values.size(); i++) {
        cout << "(";
        cout << values[i].first << ", " << values[i].second;
        cout << "), ";
    }
    cout << endl;

    // testing orientations
    cout << endl;
    cout << "Orientation testing ";
    cout << orientation(values[0], values[1], values[2]) << endl;

    unordered_map<string, vector<pair<int, int>>> caps = all_convex(values);
    int count = 0;
    for (auto conv: caps) {
        cout << "Conv number " << count << endl;
        for (int i = 0; i < conv.second.size(); i++) {
            cout << conv.second[i].first << " " << conv.second[i].second << endl;
        }
        cout << endl << endl;
        count++;
    }
    return 0;
}
