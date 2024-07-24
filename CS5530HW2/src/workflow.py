# This file executes the data workflow
# 
import data_work
import glucose
import bmi
import bootstrap

def main():
    data_work.run()
    glucose.run()
    bmi.run()
    bootstrap.run()

if __name__ == "__main__":
    main()
