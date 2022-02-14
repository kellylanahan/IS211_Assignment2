import argparse
import datetime
import logging


def downloadData(url):
    return urllib2.urlopen(url)


def processData(infile):
    processed_data = {}
    csv_reader = csv.reader(infile)
    next(csv_reader)

    for i, person in enumerate(csv_reader):
        try:
            p_id = int(person[0])
            p_name = person[1]
            p_birth_date = datetime.datetime.strptime(person[2], "%d/%m/%Y")
            processed_data[p_id] = (p_name, p_birth_date)

        except:
            error_msg = "Error processing line #{} for ID #{}.".format(i, p_id)
            logging.basicConfig(filename="error.log", level=logging.ERROR)
            logger = logging.getLogger("assignment2")
            logger.error(error_msg)

    return processed_data


def displayPerson(pid, dict_data):
    if pid in dict_data:
        name = dict_data[pid][0]
        bdate = datetime.datetime.strftime(dict_data[pid][1], "%Y-%m-%d")

        print("Person #{} is {}  with a birthday of {}.".format(pid, name, bdate))

    else:
        print("No user found with that id.")


def main():
    downloaded_data = None
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="Provide the csv file's URL.")
    args = parser.parse_args()
    try:
        downloaded_data = downloadData(args.url)
    except:
        print("Error occurred while downloading the file !!!")
    process_dict = processData(downloaded_data)
    while True:
        pid = int(input("Enter ID to lookup: "))
        if pid <= 0:
            break
        else:
            displayPerson(pid, process_dict)


if __name__ == "__main__":
    main()