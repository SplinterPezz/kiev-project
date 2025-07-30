import { utilsService } from '../utils/utils.js'
import * as Constants from '../Constants.js'

const {handleResponse} = utilsService

export const chartService = {
  getDeathEnjuried,
  getTotalDeath,
  getTotalEquipment,
  getDeathEquipment,
  getTreeTag,
  getArticlesDeath,
  getFirePower,
  getRefugeesDaily,
  getRefugeesAggregated
}

function getRefugeesAggregated(){
  const requestOptions = {
    method: "GET",
  };
  const thisUrl = Constants.URL + '/chart/refugees-aggregated/'
  
  return fetch(
    thisUrl,
    requestOptions
  )

  .then(handleResponse)
  .then(res => {
    return res;
  });
}

function getRefugeesDaily(days){
  const requestOptions = {
    method: "GET",
  };
  const thisUrl = Constants.URL + '/chart/refugees-daily/' + days
  
  return fetch(
    thisUrl,
    requestOptions
  )

  .then(handleResponse)
  .then(res => {
    return res;
  });
}

function getDeathEnjuried(type, days){
  const requestOptions = {
    method: "GET",
  };
  const thisUrl = Constants.URL + '/chart/death-enjuried/' + type + '/' + days
  
  return fetch(
    thisUrl,
    requestOptions
  )

  .then(handleResponse)
  .then(res => {
    return res;
  });
}

function getFirePower(){
  const requestOptions = {
    method: "GET",
  };
  const thisUrl = Constants.URL + '/chart/fire-power/'
  
  return fetch(
    thisUrl,
    requestOptions
  )

  .then(handleResponse)
  .then(res => {
    return res;
  });
}

function getTotalDeath(type, days, sumType){
  const requestOptions = {
    method: "GET",
  };
  const thisUrl = Constants.URL + '/chart/death/' + type + "/" + days + "/" + sumType
  
  return fetch(
    thisUrl,
    requestOptions
  )

  .then(handleResponse)
  .then(res => {
    return res;
  });
}

function getTotalEquipment(days, sumType){
  const requestOptions = {
    method: "GET",
  };
  const thisUrl = Constants.URL + '/chart/equipment/' + days + "/" + sumType
  
  return fetch(
    thisUrl,
    requestOptions
  )

  .then(handleResponse)
  .then(res => {
    return res;
  });
}

function getDeathEquipment(days){
  const requestOptions = {
    method: "GET",
  };
  const thisUrl = Constants.URL + '/chart/death-equipment/' + days
  
  return fetch(
    thisUrl,
    requestOptions
  )

  .then(handleResponse)
  .then(res => {
    return res;
  });
}


function getTreeTag(days){
  const requestOptions = {
    method: "GET",
  };
  const thisUrl = Constants.URL + '/chart/tree-tag/' + days
  
  return fetch(
    thisUrl,
    requestOptions
  )

  .then(handleResponse)
  .then(res => {
    return res;
  });
}



function getArticlesDeath(charType ,days){
  const requestOptions = {
    method: "GET",
  };
  const thisUrl = Constants.URL + '/chart/' + charType + '/' + days
  
  return fetch(
    thisUrl,
    requestOptions
  )

  .then(handleResponse)
  .then(res => {
    return res;
  });
}
