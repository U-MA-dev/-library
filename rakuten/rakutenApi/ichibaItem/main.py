from bizlogic import SourceManager
from model.inputmodel import SearchConditionModel
from model.outputmodel import EntireInfoModel


def main():
    source_manager = SourceManager()

    input_model = SearchConditionModel()
    input_model.hits = 1
    input_model.genre_id = "566031"
    input_model.genre_infomation_flag = 1
    input_model.tag_information_flag = 1

    output_model: EntireInfoModel = \
        source_manager.fetch_search_info(input_model)
    for item_model in output_model.item_info_model_list:
        # print(item_model.tag_id_list)
        pass


if __name__ == "__main__":
    main()
