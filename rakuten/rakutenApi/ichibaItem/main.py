from bizlogic import SourceManager
from ichibaItem.model.inputmodel import SearchConditionModel
from ichibaItem.model.outputmodel import EntireModel

APPLICATION_ID = "1059250682711460507"
AFFILIATE_ID = "1870052b.b6952624.1870052c.f9eb35fb"


def main():
    source_manager = SourceManager(APPLICATION_ID, AFFILIATE_ID)

    input_model = SearchConditionModel()
    input_model.hits = 1
    input_model.genre_id = "566031"
    input_model.genre_infomation_flag = 1
    input_model.tag_information_flag = 1

    output_model: EntireModel = \
        source_manager.fetch_search_info(input_model)
    for item_model in output_model.item_model_list:
        # print(item_model.tag_id_list)
        pass


if __name__ == "__main__":
    main()
