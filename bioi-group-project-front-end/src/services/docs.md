Services are functions built to support the VueJS front end. Many of the functions are used to send HTTP requests to the API using the package Axios.

## authHeader
Writes the header to be sent for authenticating that the user is logged in.

Grabs the user data stored in local storage upon a successful login, and creates a JSON object containing the access token, username, and userID.

```jsx static
export default function authHeader() {
    let user = JSON.parse(localStorage.getItem('user'));
    console.log(user)
    if (user && user.token) {
        console.log("Found User")
        return { 'x-access-token': user.token,
                 'username': user.username,
                 'userId': user.userId};
    }
    else {
        return {};
    }
}
```

## Data Visualization Service
Contains functions to support the data visualization functionality

### Imports
- Axios - 'axios'

### Functions

getVaccineData() - Sends an HTTP GET request to the API

**Params:**
vaccineParams *[JSON object]* - contains state, age range, and vaccine type.

```jsx static
async getVaccineData(vaccineParams) {
        let res = await axios.get((local + "/api/getVaccineData"), {params: {state: vaccineParams.state, ages: vaccineParams.ages, vaxType: vaccineParams.vaxType}});
        return res;
    }
```

## Card Visualization Service
Contains functions to support the vaccine card storage/retrieval functionality

### Imports
- Axios - 'axios'
- router - '../router'
- authHeader - './authHeader'

### Functions

createUser() - Sends an HTTP POST request to the API containing a user to be added to the database

**Params:**
userParams *[JSON object]* - contains the username, password, and vaccine card image to be added to the database

```jsx static 
async createUser(userParams) {
        console.log(userParams)
        let res = await axios.post((local + "/api/createUser"), userParams, { headers: {
            'Content-Type': 'multipart/form-data' }
          })
        return res;
    }
```

login() - Sends an HTTP POST request to the API containing user data to be validated for login. Creates a FormData object containing the username and password which is sent to the API. Upon a successful login, the access token, username, and userID returned are stored into the local storage, and the app is redirected to the card view component. Upon a failure, it does nothing, and the user remains on the login page.  

**Params:**
user *[JSON object]* - contains the username and password being used to log in.

```jsx static 
async login(user) {
      var loginData = new FormData()
      loginData.append('username', user.username);
      loginData.append('password', user.password);
      return axios.post((local + "/api/login"), loginData, { headers: {
          'Content-Type': 'multipart/form-data' }
       })
       .then(response => {
        console.log(response)
        if (response.data.token) {
            localStorage.setItem('user', JSON.stringify(response.data));
        }
        router.push('/card')
        console.log("Success")
        })
        .catch(err => {
            err;
        });
    }
```

getCard() - Sends an HTTP GET request to the API requesting the image tied to the loggged in user. First, creates an authentication header and sends this to the API. The result is returned to the caller.

```jsx static 
async getCard() {
        var head = authHeader()
        console.log(head)
        let res = await axios.get((local + "/api/getCard"), {params: head, responseType: "blob" }, { headers: {  
            'Content-Type': 'application/json'}});

        return res;

    }
```

