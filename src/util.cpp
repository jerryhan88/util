#include "../include/ck_util/util.hpp"

void createCSV(std::string fpath, char *header) {
    if (fpath == "") {
        return;
    }
    std::fstream fout;
    fout.open(fpath, std::ios::out);
    fout << header << "\n";
    fout.close();
}

void appendRow(std::string fpath, char *row) {
    if (fpath == "") {
        return;
    }
    std::fstream fout;
    fout.open(fpath, std::ios::out | std::ios::app);
    fout << row << "\n";
    fout.close();
}

bool hasOption(std::vector<std::string> &arguments, std::string option) {
    bool hasValue = false;
    for (std::string str: arguments) {
        if (str == option) {
            hasValue = true;
        }
    }
    return hasValue;
}

std::string valueOf(std::vector<std::string> &arguments, std::string option) {
    std::string value = "";
    for (int i = 0; i < arguments.size(); i++) {
        if (arguments[i] == option) {
            value = arguments[i + 1];
        }
    }
    return value;
}

std::vector<std::string> parseWithDelimiter(std::string str, std::string delimiter) {
    std::vector<std::string> tokens;
    size_t pos = 0;
    std::string token;
    while ((pos = str.find(delimiter)) != std::string::npos) {
        token = str.substr(0, pos);
        tokens.push_back(token);
        str.erase(0, pos + delimiter.length());
    }
    tokens.push_back(str);
    return tokens;
    
}

std::vector<std::string> read_directory(const std::string &d_path, const std::string &extension) {
    std::vector<std::string> fileNames;
    DIR* dirp = opendir(d_path.c_str());
    struct dirent * dp;
    while ((dp = readdir(dirp)) != NULL) {
        std::string fn(dp->d_name);
        std::size_t found = fn.find(extension);
        if (found!=std::string::npos)
            fileNames.push_back(fn);
    }
    closedir(dirp);
    std::sort(fileNames.begin(), fileNames.end());
    return fileNames;
}

std::string TimeTracker::get_curTime() {
    time_t now = time(0);
    char* dt = ctime(&now);
    return std::string(dt);
}

double TimeTracker::get_elapsedTimeCPU() {
    std::clock_t c_end = std::clock();
    return (c_end-c_start) / (double) CLOCKS_PER_SEC;
}

double TimeTracker::get_elapsedTimeWall() {
    std::chrono::high_resolution_clock::time_point w_end = std::chrono::high_resolution_clock::now();
    return std::chrono::duration<double, std::milli>(w_end-w_start).count() / 1000.0;
}


