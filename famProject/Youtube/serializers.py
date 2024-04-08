class YoutubeVideoListSerializer():

    def __init__(self):
        pass

    @staticmethod
    def serializer(queryset):
        result = []
        count = 0
        for data in queryset:
            count+=1
            temp_res = {}
            for key, value in data.items():
                temp_res[key] = value
            result.append(temp_res)
        return result, count