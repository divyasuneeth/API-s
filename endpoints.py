from flask import Flask,request
app = Flask(__name__)
# Create the appropriate app.route functions. Test and see if they work

#Make an app.route() decorator here for when the client sends the URI "/puppies"
@app.route("/puppies",methods=['GET','POST'])
def puppiesFunction():
    if request.method=='GET':
        return getAllPuppies()
    elif request.method=='POST':
        return makeANewPuppy()



#Make another app.route() decorator here that takes in an integer named 'id' for when the client visits a URI like "/puppies/5"
@app.route("/puppies/<int:id>",methods=['GET','PUT','DELETE'])
def puppiesFunctionId(id):
    if request.method=='GET':
        return getPuppy(id)
    if request.method=='PUT':
        return updatePuppy(id)
    if request.method=='DELETE':
         return deletePuppy(id)


def getAllPuppies():
    return "Getting all puppies!"

def makeANewPuppy():
    return "Creating A New Puppy!"

def getPuppy(id):
    return "Getting Puppy with id %s"% id

def updatePuppy(id):
    return "Updating a Puppy with id %s" % id

def deletePuppy(id):
    return "Removing Puppy with id %s" %id



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
