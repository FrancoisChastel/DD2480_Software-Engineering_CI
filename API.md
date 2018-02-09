# API Documentation
This API.md allows to understand better how to reach the API with a well formed JSON
Please read the README.md before going further in the lecture of this documentation.

## End-point
To reach the API you need get the IP address of your server and reach the method `/postreceive`
Once it's done you need to send a `POST` query to this address with a well-formed JSON and the right header.

## JSON
The JSON need to be formed as follow (you can have more attributes:
```
{
  "head_commit": {
    "id": "8bb929891b4861563b5abfd4899c1b6ce25776f1",
    "tree_id": "b8b0fc617c9f3a8380b635974236e6d38fb738c6",
    "distinct": true,
    "message": "issue #2 #3 #4 #7, docs: adding comments to all the useful function",
    "timestamp": "2018-02-09T17:40:36+01:00",
    "url": "https://github.com/FrancoisChastel/DD2480_Software-Engineering_CI/commit/8bb929891b4861563b5abfd4899c1b6ce25776f1",
    "author": {
      "name": "François Chastel",
      "email": "francois@chastel.co",
      "username": "FrancoisChastel"
    },
    "committer": {
      "name": "François Chastel",
      "email": "francois@chastel.co",
      "username": "FrancoisChastel"
    }
  },
  "repository": {
    "id": 119710877,
    "name": "DD2480_Software-Engineering_CI",
    "owner": {
      "name": "FrancoisChastel",
      "email": "FrancoisChastel@users.noreply.github.com",
      "login": "FrancoisChastel",
      "url": "https://api.github.com/users/FrancoisChastel",
    }
  }
}
```
