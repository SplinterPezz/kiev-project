export const utilsService = {
  handleResponse
};


function handleResponse(response) {
    return response.text().then(text => {
      const data = text && JSON.parse(text);
      if (!response.ok) {
        switch(response.status){
          case 401:
             // auto logout if 401 response returned from api
            // userService.logout();
            window.location.reload(true);
            break;
          case 409:
            return Promise.resolve({...data, statusCode: 409})
          
          default:
            return Promise.resolve({...data, statusCode: 500})
        }
      
      const error = (data && data.message) || response.statusText;
      return Promise.reject(error);
    }

    return data;
  });
}