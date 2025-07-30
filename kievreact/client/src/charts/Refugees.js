import React from "react";
import ReactApexChart from "react-apexcharts";
import '../App.css';
import { Card, InputNumber, Button, Space, message } from 'antd';
import { chartService } from '../services/chart.service'
import { chartOption } from '../utils/chart.option'

const importedOptions = chartOption.getCommonChart()
const default_days = 19
class Refugees extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      seriesDaily: [],
      seriesAggregated: [],
      optionsDaily:{
        ...importedOptions
      },
      optionsAggregated:{
        ...importedOptions
      },
      days : default_days
    };
  }

  setDays(days) {
    if(days !== undefined){
      this.setState({
        days: days
      });
      this.getRefugeesDaily(days);
    }
    
  }

  componentDidMount() {
    this.getRefugeesDaily(default_days);
    this.getRefugeesAggregated();
  }

  getRefugeesDaily = (days) => {
    chartService.getRefugeesDaily(days).then(res => {
      this.setState({
        seriesDaily: res.series,
        optionsDaily: {
          xaxis: res.xaxis
        }
      });
    },
    error=>{
      console.log('ERROR',error)
      message.error(`An error occurred during getting refugees daily chart`);
    });
  };

  getRefugeesAggregated = () => {
    chartService.getRefugeesAggregated().then(res => {
      this.setState({
        seriesAggregated: res.series,
        optionsAggregated: {
          xaxis: res.xaxis
        }
      });
    },
    error=>{
      console.log('ERROR',error)
      message.error(`An error occurred during getting refugees aggregated chart`);
    });
  };

  render() {
    return (
      <div className="site-card-border-less-wrapper">
        <Card title={"Refugees per days by nations"} bordered={false} className="mt-5"extra={
          <Space>
              <InputNumber min={1} max={99} value={this.state.days} onChange={(e) => this.setDays(e)} />
              <Button type="primary" onClick={() => { this.setDays(default_days); }}>
                  Reset
              </Button>
          </Space>
          }>
          <div className="app">
            <div className="row">
              <div className="col-12 col-lg-6">
                <div className="mixed-chart">
                  <div id="chart">
                    <ReactApexChart options={this.state.optionsAggregated} series={this.state.seriesAggregated} height={"350px"} type="bar" />
                  </div>
                </div>
              </div>
              <div className="col-12 col-lg-6">
                <div className="mixed-chart">
                  <div id="chart">
                    <ReactApexChart options={this.state.optionsDaily} series={this.state.seriesDaily} height={"350px"} type="bar" />
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


export default Refugees;
