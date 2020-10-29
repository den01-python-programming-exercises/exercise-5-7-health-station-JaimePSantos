# from health_station import HealthStation
# from person import Person
def main():

    childrens_hospital = HealthStation()

    ethan = Person("Ethan", 1, 110, 7)
    peter = Person("Peter", 33, 176, 85)

    # print("weighings performed: " + childrens_hospital.weighings())

    childrens_hospital.weigh(ethan)
    childrens_hospital.weigh(peter)

    # print("weighings performed: " + childrens_hospital.weighings())

    childrens_hospital.weigh(ethan)
    childrens_hospital.weigh(ethan)
    childrens_hospital.weigh(ethan)
    childrens_hospital.weigh(ethan)

    # print("weighings performed: " + childrens_hospital.weighings())

if __name__ == '__main__':
  from health_station import HealthStation
  from person import Person
  main()
  
else:
  from src.health_station import HealthStation
  from src.person import Person

