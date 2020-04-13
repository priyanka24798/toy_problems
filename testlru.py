from lrucache import lrucache

class unit_test:
    

    def __init__(self):
        pass

    def test_cases(self):
        a = lrucache(4)
        a.put("priya")
        a.put("hari")
        a.put("abhi")
        a.put("sunny")
        assert a.get("priya") == "priya is from IIIT hyderabad", "case 1 failed"
        assert a.get("abhi") == "abhi is from IIIT hyderabad", "case 2 failed"
        assert a.get("hari") == "hari is from IIIT hyderabad", "case 3 failed"
        assert a.get("sunny") == "sunny is from IIIT hyderabad", "case 4 failed"
        a.put("priya") == None, "testcase failed"
        print("All passed..!")
       
       #to print the cache items:
        l = a.get_cache()
        print(l)

if __name__ == '__main__':
    a = unit_test()
    a.test_cases()

 

    







