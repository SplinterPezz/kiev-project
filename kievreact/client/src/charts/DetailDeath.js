import React from "react";
import ReactApexChart from "react-apexcharts";
import '../App.css';
import { Card, InputNumber, Button, Space, message } from 'antd';
import { chartService } from '../services/chart.service'
import { chartOption } from '../utils/chart.option'

const default_days = 14
var importedOptions = chartOption.getStackedChart();

class DetailDeath extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      series: [],
      options: { 
        ...importedOptions
      },
      type: props.type,
      days: default_days
    };
  }

  setDays(days) {
    if(days !== undefined){
      this.setState({
        days: days
      });
      this.getDeathEnjuriedChart(this.state.type, days)
    }
    
  }

  componentDidMount() {
    this.getDeathEnjuriedChart(this.state.type, default_days)
  }

  getDeathEnjuriedChart = (type, days) => {

    chartService.getDeathEnjuried(type, days).then(res => {

      this.setState({
        series: res.series,
        options: {
          xaxis: res.xaxis
        }
      });
    },
    error=>{
      console.log('ERROR',error)
      message.error(`An error occurred during getting detail death chart`);
    });
  }

  render() {
    return (
      <div className="site-card-border-less-wrapper">
        <Card title={(this.state.type).toUpperCase().charAt(0).toUpperCase() + this.state.type.slice(1) + " Details"} bordered={false} extra={
          <Space>
            <InputNumber min={1} max={99} value={this.state.days} onChange={(e) => this.setDays(e)} />
            <Button type="primary" onClick={() => { this.setDays(default_days); }}>
              Reset
            </Button>
          </Space>
        }>
          <div className="app">
            <div className="row">
              <div className="mixed-chart">
                <div id="chart">
                  <ReactApexChart options={this.state.options} series={this.state.series} type="bar" height={350} />
                </div>
              </div>
            </div>
          </div>
        </Card>
      </div>
    );
  }
}


export default DetailDeath;
