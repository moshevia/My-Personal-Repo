from transifex.api import TransifexAPI
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("language") 	# naming it "language"
args = parser.parse_args() 	# returns data from the options specified
print args.language


def get_translation_transifix(lang, username="jenkins_user", password="Jenkins1!"):
    # print args.language
    t = TransifexAPI(username, password, 'https://www.transifex.com')
    # check success connection to transefix database
    print t.ping()
    print "connected to database"
    #check if project exists
    print t.project_exists("via-operational-center")
    print "found the via translations project"
    list1 = t.list_resources("via-operational-center")
    print list1

    t.get_translation('via-operational-center', "voc-fe-en-usjson", lang,
                      "/translation.json")

    with open("translation.json", "a") as f:
        f.write("; \n export default translations")

    with open("translation.json", "r+") as f:
        origin = f.read()  # read everything in the file
        f.seek(0)  # rewind
        f.write("import {Translations} from \"src/constants/locales/translations\"; "
                "\n\nconst translations: Translations = " + origin)
    print "finished successfully!"
    return


get_translation_transifix(args.language)

