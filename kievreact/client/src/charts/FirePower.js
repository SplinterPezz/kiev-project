import React from "react";
import ReactApexChart from "react-apexcharts";
import '../App.css';
import { Card, message } from 'antd';
import { chartService } from '../services/chart.service'
import { chartOption } from '../utils/chart.option'

const importedOptions = chartOption.getCommonChart()

class FirePower extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      optionsPower:{
        ...importedOptions
      },
      optionsResources:{
        ...importedOptions
      },
      seriesPower: [],
      seriesResources: [],
    };
  }

  componentDidMount() {
    this.getFirePowerChart()
  }

  getFirePowerChart = () => {
    chartService.getFirePower().then(res => {
      this.setState({
        seriesPower: res['power'].series,
        optionsPower: {
          xaxis: res['power'].xaxis
        },
        seriesResources: res['resources'].series,
        optionsResources: {
          xaxis: res['resources'].xaxis
        }
      });
    },
    error=>{
      console.log('ERROR',error)
      message.error(`An error occurred during getting fire power chart`);
    });
  }

  render() {
    return (
      <div className="site-card-border-less-wrapper">
        <Card title={"FirePower Details compared to other Nations"} bordered={false} className="mt-5">
          <div className="app">
            <div className="row">
              <div className="col-12 col-lg-6">
                <div className="mixed-chart">
                  <div id="chart">
                    <ReactApexChart options={this.state.optionsPower} series={this.state.seriesPower} type="bar" height={350} />
                  </div>
                </div>
              </div>
              <div className="col-12 col-lg-6">
                <div className="mixed-chart">
                  <div id="chart">
                    <ReactApexChart options={this.state.optionsResources} series={this.state.seriesResources} type="bar" height={350} />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </Card>
      </div>
    );
  }
}


export default FirePower;
