from Person import Person
import pickle

class FamilyTree:
  def __init__(self):
    self.treeNodes = dict()
    

  
  #Method to find the parent, if person is root (Origin) of the familyTree, it returns None
  def findParent(self,person):
    if person is None:
      return None
    for parent, children in self.treeNodes.items():
      for child in children:
        if child == person:
          return parent
    return None

  #Using BFS
  def findPerson(self, person):
    print(person.firstName, person.lastName)
    if person is None:
      return False
    if self.rootParent:
      visited = []
      queue = []   
      root = self.rootParent
      pt =  (person.firstName, person.lastName)
      visited.append(root)
      queue.append(root)
      matchedPerson = []
      while queue:
        s = queue.pop(0)
        rt = (s.firstName, s.lastName)
        if (rt == pt):
          matchedPerson.append(s)
        for neighbour in self.treeNodes[s]:
          if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour) 
    return matchedPerson
  #Method to find all Ancestor of a given Person in the Family Tree
  def findAncestor(self,person):
    if person is None:
      return None
    anestors = []
    parent = person
    while (parent):
      parent = self.findParent(parent)
      anestors.append(parent)
    return anestors[:-1]
  
  #Method to find the grandParent of the person or None if the grandParent is not present
  def findGrandParent(self,person):
    parent = self.findParent(person)
    grandParent = self.findParent(parent)
    return grandParent

  #Method to Add a person to a family Tree
  def addPerson(self,person):
    if person is None:
      print("Person cannot be none")
      return False
    if person not in self.treeNodes:
      self.treeNodes[person] = []
    else:
     print(str(person) + " already present")
 

  #Sets a the given person as the root of the familyTree
  def setRootParent(self,person):
    if person is not None and person in self.treeNodes:
      self.rootParent = person


  #Connects two persons. If the second person is connected to another parent, removes the connection and connects with the first person
  def linkPersons(self,personA,personB):
    if personA == personB:
      print("Same Person")
      return False
    if personA in self.treeNodes and personB in self.treeNodes:
       parent = self.findParent(personB)
       if parent is not None:
         children = self.treeNodes[parent]
         children.remove(personB)
       vals = self.treeNodes[personA]
       if personB not in vals:
          vals.append(personB)
    else:
       print("Add " + str(personA))


  #Private Method. Removes a given person from the Tree
  def __removePerson(self,person):
    if person in self.treeNodes:
      parent = self.findParent(person)
      if parent is not None:
        children = self.treeNodes[parent]
        children.remove(person)
      del self.treeNodes[person]

  #Method to remove a person and their children
  def removePersonAndChildren(self,person):
      if person in self.treeNodes:
        children = self.treeNodes[person]
        self.__removePerson(person)
        for child in children:
          self.removePersonAndChildren(child)
   
  
  #Private Method that does the printing work
  def __printTreeHelperFunction(self,person,spaces):
    if person is not None:
      print(spaces + str(person))
      children = self.treeNodes[person]
      for child in children:
        self.__printTreeHelperFunction(child,spaces + '\t')

  
  #Public method for printing the tree
  def printTree(self):
    if hasattr(self,"rootParent") is True: #checking if the rootParent Person exist in the self(FamilyTree)
      self.__printTreeHelperFunction(self.rootParent,'')
    else:
      print("Please, first set the rootParent using setRootParent method")

  
  #Returns a string representation of the family tree
  def __str__(self):
   objStr=''
   for key,value in self.treeNodes.items():
     objStr = objStr + str(key) + ":["
     for person in value:
         objStr=objStr+ str(person)+", "
     objStr = objStr + "]\n"
   return objStr
   
  
  #Serialize the family and store it in  a file using pickle module
  def saveTree(self,filename):
    if filename is not None and len(filename) > 0: 
      f= open(filename, "wb")
      pickle.dump(self, f)
    else:
        print("Error pickling the object")

  def loadFamilyTree(self,filename):
    if filename is not None and len(filename) > 0:
      f = open(filename, 'rb')
      self = pickle.load(f)
      return self
    else:
      print("Error loading the object")
  

# ----------------Driver Program----------------#
familyTree1 = FamilyTree() 
Alex = Person("Alex","Mercer")
June = Person("June","Lisa")
Omer = Person("Omer","Ali")
Sarah = Person("Sarah","John")
Alferd = Person("Alferd","David")
Law = Person("Law","Anderson")
Little = Person("Little","Princess")
Luffy = Person("Luffy","Jesus")
Erik = Person("Erik","Muller")
Misa = Person("Misa","Erik")
FamilyMembers=[Alex,June,Omer,Sarah,Alferd,Law,Little,Luffy,Erik,Misa] 
for member in FamilyMembers:
  familyTree1.addPerson(member)

#linkPersons(Parent, Child)
familyTree1.linkPersons(Alex,Omer)
familyTree1.linkPersons(Alex,Alferd)
familyTree1.linkPersons(Alex,June)
familyTree1.linkPersons(Omer,Sarah)
familyTree1.linkPersons(Alferd,Law)
familyTree1.linkPersons(Alferd,Little)
familyTree1.linkPersons(Law,Luffy)
familyTree1.linkPersons(Sarah,Erik)
familyTree1.linkPersons(Sarah,Misa)
familyTree1.setRootParent(Alex)
familyTree1.printTree()
familyTree1.saveTree("family.txt")

p = familyTree1.findParent(Erik)
gp = familyTree1.findGrandParent(Erik)


anecestors = familyTree1.findAncestor(Erik)
for i in range(len(anecestors)):
  print(anecestors[i])


#Testing loading of Object from drive
print("\n\nFamily Tree 2")
familyTree2 = FamilyTree()
familyTree2 = familyTree2.loadFamilyTree('family.txt')
familyTree2.printTree()

match = familyTree2.findPerson(Alex)
print()
print(match)