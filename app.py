from flask import Flask , request

app = Flask(__name__)

#create the idea repository 
ideas = {
    1 : {
        "id" : 1,
        "idea_name" : "ONDC",
        "idea_description" : "Detail about ONDC",
        "idea_author" : "Ansh sharma"
    },
    2 : {
        "id" : 2,
        "idea_name" : "Save soil",
        "idea_description" : "Detail about soil",
        "idea_author" : "Anshika sharma"
    },
    3 : {
        "id" : 3,
        "idea_name" : "Save earth",
        "idea_description" : "Detail about earth",
        "idea_author" : "vishwa sharma"
    }
}

#create the restfull end to end api

@app.get("/ideaapp/api/v1/ideas")
def get_all_idea():
    #logic to fetch all the ideas and support query param
    idea_author = request.args.get("idea_author")
    if idea_author:
        #filter the idea creates by this author 
        ideas_res = {}
        for key , value in ideas.items():
            if value["idea_author"] == idea_author:
                ideas_res[key] = value
        return ideas_res
    return ideas

# create the restful endpoint for creating a new idea
@app.post("/ideaapp/api/v1/ideas")
def creat_idea():
    #logic to create a new idea
    try:
        # first read the request body
        request_body = request.get_json()

        # check  if the idea id passed  is not present already
        if request_body["id"] and  request_body["id"] in ideas:
            return "idea with the same id already present",400

        # insert the passed idea in the odea dictionary
        ideas[request_body["id"]] = request_body

        # return the response 
        return "idea created and saved succesfully",201
    except KeyError:
        return "id is missing",401
    except:
        return "something internal  server error",500

# End point to fetch  idea based on the idea id 
@app.post("/ideaapp/api/v1/ideas/<idea_id>")
def get_idea_id(idea_id):
    try:
        if int(idea_id) in ideas : 
            return  ideas[int(idea_id)],200
        else:
            return "idea id passed is not present",400

    except:
        return "Some internal error happend",500

# End point to update  idea based on the idea id 
@app.put("/ideaapp/api/v1/ideas/<idea_id>")
def update_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas[int(idea_id)] = request.get_json()
            return ideas[int(idea_id)],200
        else:
            return "Idea id passed is not present",400 
    except: 
        return "some internal error happened" ,500


# End point to delete an idea
@app.delete("/ideaapp/api/v1/ideas/<idea_id>")
def delete_idea(idea_id):
    try:
        if int(idea_id) in ideas:
           ideas.pop(int(idea_id))
           return "Idea got succesfull removed "
        else:
            return "Idea id passed is not present",400 
    except: 
        return "some internal error happened" ,500



if __name__ == '__main__':
    app.run(port=8080)