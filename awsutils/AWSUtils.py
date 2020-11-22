import boto3

class AWSUtils:

    def get_key_pair_name(self):

        aws_client = boto3.client('ec2')
        key_pairs_list = aws_client.describe_key_pairs()["KeyPairs"]

        if len(key_pairs_list) == 0:
            return None
        elif len(key_pairs_list) == 1:
            return key_pairs_list[0]["KeyName"]
        else:
            return self.__choose_between_keypairs(key_pairs_list)

    def guessLocalProfile(self):
        profile_list = boto3.session.Session().available_profiles
        if len(profile_list) == 1:
            return profile_list[0]
        if len(profile_list) > 1 and 'default' in profile_list:
            return 'default'
        return ""

    def get_regions_name(self) -> list:
        aws_client = boto3.client('ec2')
        region_names = []
        for region_name in aws_client.describe_regions()["Regions"]:
            region_names.append(region_name["RegionName"])
        return region_names

    def __choose_between_keypairs(self, keypairs_result) -> str:
        cleaned_keypairs_name_results = []
        key_pair_message_part = ""
        for singlekey in keypairs_result:
            singleKeyName = singlekey["KeyName"]
            cleaned_keypairs_name_results.append(singleKeyName)
            key_pair_message_part += " * " + singleKeyName + "\n"
        choosing_message = "It was found several keypairs on your account:\n"
        choosing_message += key_pair_message_part
        choosing_message += "Choose one, typing the name: "
        choosed_message = input(choosing_message)
        if not choosed_message in cleaned_keypairs_name_results:
            raise Exception("You provided an invalid message.")
        return choosed_message