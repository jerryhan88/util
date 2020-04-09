//
//  util.hpp
//
//  Created by Chung-Kyun HAN on 27/2/20.
//  Copyright © 2020 Chung-Kyun HAN. All rights reserved.
//

#ifndef util_hpp
#define util_hpp

#include <dirent.h>
#include <string>
#include <vector>
#include <fstream>
#include <ctime>
#include <chrono>
#include <algorithm>


void createCSV(std::string fpath, char *header);

void appendRow(std::string fpath, char *row);

bool hasOption(std::vector<std::string> &arguments, std::string option);

std::string valueOf(std::vector<std::string> &arguments, std::string option);

std::vector<std::string> parseWithDelimiter(std::string str, std::string delimiter);

std::vector<std::string> read_directory(const std::string &d_path, const std::string &extension);


class TimeTracker {
public:
    std::clock_t c_start;
    std::chrono::high_resolution_clock::time_point w_start;
    //
    TimeTracker() {
        c_start = std::clock();
        w_start = std::chrono::high_resolution_clock::now();
    }
    ~TimeTracker() {}
    //
    std::string get_curTime();
    double get_elapsedTimeCPU();
    double get_elapsedTimeWall();
};

class FilePathOrganizer {
public:
    std::string logPath, solPathCSV, solPathTXT, lpPath, ilpPath;
    //
    FilePathOrganizer(const std::string &appr_dpath, const std::string &postfix) {
		std::string appr_name = appr_dpath.substr(appr_dpath.find_last_of("/") + 1, appr_dpath.size());
		std::string prefix(appr_dpath + "/" + appr_name + "_" + postfix);
		//
		this->logPath = prefix + ".log";
		this->solPathCSV = prefix + ".csv";
		this->solPathTXT = prefix + ".txt";
		this->lpPath = prefix + ".lp";
		this->ilpPath = prefix + ".ilp";
    }
    ~FilePathOrganizer() {}
};

#endif
