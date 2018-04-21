import argparse
from wiki_440_version_helper import Version_Helper




def edit_file(args, path):

    """
    author: Jasper Bichler
    date: 4/20/2018
    returns message dictating the status of the process

    """

    message = ""
    myf = open(path, 'r')
    contents = myf.read()

    if args.e == 'upper':
        contents = contents.upper()
        message += "File contents changed to upper case, and saved as a new version\n"

    if args.e == 'lower':
        contents = contents.lower()
        message += "File contents changed to lower case and saved as a new version\n"

    message += save(path, contents)
    myf.close()

    return message


def save(path, contents):

    """
    author: Jasper Bichler
    date: 4/20/2018
    saves a new version of the edited file

    """

    file_name = None

    if Version_Helper.get_highest_version_of_file_path(path) is not None:
        file_name = Version_Helper.get_highest_version_of_file_path(path)
    else:
        file_name = Version_Helper.get_filename_from_path(path)

    file_ext = file_name.rsplit('.', 1)
    file_name = file_ext[0]
    extension = file_ext[1]
    version_no = 0

    index = len(file_name)

    if not file_name[index-1].isdigit():
        version_no = 1
    else:
        version_no = int(file_name[index-1]) + 1
        file_ext = file_name.rsplit('_', 1)

    newest_versioned__path = file_ext[0] + '_v' + str(version_no) + '.' + extension

    newf = open(newest_versioned__path, 'w+')

    for line in contents:
      newf.write(line)

    newf.close()

    return "Changes saved"


if __name__ == '__main__':

    message = None
    parser = None

    parser = argparse.ArgumentParser()

    parser.add_argument('-p', help='Path to the file you want to change, or "close" to close the opened file')
    parser.add_argument('-e', help='upper to change case of the contents to upper case, lower for lower case')
    args = parser.parse_args()

    if args.p is not None:
        message = edit_file(args, args.p)

    else:
        message = "Please enter the path of a file to edit"

    print message

