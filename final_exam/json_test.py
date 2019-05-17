# Sample

import json

class Person:
    def __init__(self, name, choices, idx):
        self.name = name
        self.choices = choices[:]
        self.idx = idx

def main():
    """
    names = [
        "Jason", "Ryan", "Des-MASSIVE"
    ]
    choices = [
        [ "Woof", "SirWoof", "TheLoneWoof"],
        [ "Partial", "PartialOff", "50%Off"],
        [ "Tiny", "Smol"]
    ]
    indices = [
        1, 0, 1
    ]

    sample_list = []
    for i in range(3):
        sample_list.append(
            {
                "name": names[i],
                "choice": choices[i][:],
                "index": indices[i]
            }
        )

    # print(json.dumps(sample_list, indent=4))
    try:
        sample_file = open("sample.json", "w")
        sample_file.write(json.dumps(sample_list, indent=4))

        sample_file.close()
    except IOError:
        print("FUCK")
        quit()

    # print(sample_list)
    """
    try:
        samp_file = open("sample.json", "r")
        samp_list = json.load(samp_file)
        samp_file.close()
    except IOError:
        print("FUCK2")
        quit()

    for item in samp_list:
        print("Name: {}".format(item["name"]))
        for choice in item["choice"]:
            print(" - {}".format(choice))
        print("Index: {}".format(item["index"]))
        print()



main()
