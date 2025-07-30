import { ACTIVE_ENV } from './env.js';

//const LOCALHOST_ENV = "localhost"
const DEVELOP_ENV = "develop"
//const STAGE_ENV = "stage"
//const MASTER_ENV = "master"

var default_url = 'http://localhost:5000'
var default_api_ver = "/v1"

if(ACTIVE_ENV === DEVELOP_ENV){
    default_url = "http://62.171.175.242:3001"
}

export const URL = default_url+default_api_ver;
