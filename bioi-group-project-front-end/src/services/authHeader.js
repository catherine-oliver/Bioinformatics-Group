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