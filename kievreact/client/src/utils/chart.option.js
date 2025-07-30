export const chartOption = {
  getStackedChart,
  getSplittedChart,
  getHeatMapChart,
  getTreeMapChart,
  getCommonChart
}

function getStackedChart() {
  return STACKED_CHART
}

function getSplittedChart() {
  return SPLITTED_CHART
}

function getHeatMapChart() {
  return HEAT_MAP_CHART
}

function getTreeMapChart(){
  return TREEMAP_CHART;
}

function getCommonChart(){
  return COMMON_CHART
}


/*
** CHARTS UTILS
*/

let ENABLED_TRUE = {
  enabled: true
}

let ENABLED_FALSE = {
  enabled: false
}

let LEGEND_ONE = {
  position: 'bottom',
  offsetX: -10,
  offsetY: 0
}

let PLOT_ONE = {
  bar: {
    horizontal: false,
    borderRadius: 5
  },
}

let FILL_ONE = {
  opacity: 1
}

let COLOR_ONE = ["#008FFB"]

let DOWNLOAD_FALSE = {
  download: false,
}

/*
** CHARTS SPECS LVL 1
*/

let SHOW_TRUE_DOWNLOAD_FALSE = {
  show: true,
  tools: DOWNLOAD_FALSE
}

let RESPONSIVE_ONE = [{
  breakpoint: 480,
  options: {
    legend: LEGEND_ONE
  }
}]

/*
** CHARTS SPECS LVL 2
*/

let CHART_ONE = {
  type: 'bar',
  stacked: true,
  toolbar: SHOW_TRUE_DOWNLOAD_FALSE,
  zoom: ENABLED_TRUE
}

let CHART_TWO = {
  type: 'bar',
  stacked: false,
  toolbar: SHOW_TRUE_DOWNLOAD_FALSE,
  zoom: ENABLED_TRUE
}

let CHART_THREE = {
  type: 'treemap',
  toolbar: SHOW_TRUE_DOWNLOAD_FALSE
}

/*
** CHARTS OBJECT TO SERVICES
*/

let STACKED_CHART = {
  chart: CHART_ONE,
  responsive: RESPONSIVE_ONE,
  plotOptions: PLOT_ONE,
  fill: FILL_ONE
}

let SPLITTED_CHART = {
  chart: CHART_TWO,
  responsive: RESPONSIVE_ONE,
  plotOptions: PLOT_ONE,
  fill: FILL_ONE,
}

let COMMON_CHART = {
  chart : CHART_TWO,
  dataLabels: ENABLED_FALSE
}

let HEAT_MAP_CHART = {
  chart : CHART_TWO,
  colors: COLOR_ONE,
  dataLabels: ENABLED_FALSE,
}

let TREEMAP_CHART = {
  chart: CHART_THREE,
}