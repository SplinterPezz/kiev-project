import React, { Component } from "react";
import Chart from "react-apexcharts";
import '../App.css';
import { Card, InputNumber, Button, Space, message } from 'antd';
import { chartService } from '../services/chart.service'
import { chartOption } from '../utils/chart.option'

const importedOptions = chartOption.getCommonChart()
const default_days = 19
class TotalDeathChart extends Component {
    constructor(props) {
        super(props);
        this.state = {
            totalChartSummed : {
                options: {
                    ...importedOptions
                },
                series : []
            },
            splittedChartSummed : {
                options: {
                    ...importedOptions
                },
                series : []
            },
            totalChartNotSummed : {
                options: {
                    ...importedOptions
                },
                series : []
            },
            splittedChartNotSummed : {
                options: {
                    ...importedOptions
                },
                series : []
            },
            days : default_days
        };
    }

    componentDidMount() {
        this.getTotalDeathChart('total', default_days, "sum");
        this.getTotalDeathChart('splitted', default_days, "sum");
        this.getTotalDeathChart('total', default_days, "sub");
        this.getTotalDeathChart('splitted', default_days, "sub");
    }

    setDays(days) {
        if(days !== undefined){
            this.setState({
                days: days
            });
            this.getTotalDeathChart('total', days, "sum");
            this.getTotalDeathChart('splitted', days, "sum");
            this.getTotalDeathChart('total', days, "sub");
            this.getTotalDeathChart('splitted', days, "sub");
        }
        
    }

    getTotalDeathChart = (type, days, sumType) => {
        chartService.getTotalDeath(type, days, sumType).then(res => {
            if(type === "total"){
                if(sumType === "sub"){
                    this.setState({
                        totalChartNotSummed : {
                            options: {
                                xaxis: res["xaxis"]
                            },
                            series: res["series"]
                        }
                    });
                }
                else{
                    this.setState({
                        totalChartSummed : {
                            options: {
                                xaxis: res["xaxis"]
                            },
                            series: res["series"]
                        }
                    });
                }
            }

            else{
                if(sumType === "sub"){
                    this.setState({
                        splittedChartNotSummed : {
                            options: {
                                xaxis: res["xaxis"]
                            },
                            series: res["series"]
                        }
                    });
                }
                else{
                    this.setState({
                        splittedChartSummed : {
                            options: {
                                xaxis: res["xaxis"]
                            },
                            series: res["series"]
                        }
                    });
                }
            }
        },
        error=>{
          console.log('ERROR',error)
          message.error(`An error occurred during getting total death chart`);
        });
    }

    render() {
        return (
            <div className="site-card-border-less-wrapper">
                <Card title="Total Death Chart" bordered={false} extra={
                    <Space>
                        <InputNumber min={1} max={99} value={this.state.days} onChange={(e) => this.setDays(e)} />
                        <Button type="primary" onClick={() => { this.setDays(default_days); }}>
                            Reset
                        </Button>
                    </Space>
                }>
                    <div className="app">
                        <div className="row">
                            <div className="mixed-chart col-12 col-lg-6">
                                <Chart
                                    height={"350px"}
                                    options={this.state.totalChartSummed.options}
                                    series={this.state.totalChartSummed.series}
                                    type="line"
                                />
                            </div>
                            <div className="mixed-chart col-12 col-lg-6">
                                <Chart
                                    height={"350px"}
                                    options={this.state.totalChartNotSummed.options}
                                    series={this.state.totalChartNotSummed.series}
                                    type="line"
                                />
                                
                            </div>
                        </div>
                        <div className="row">
                            <div className="mixed-chart col-12 col-lg-6">
                                <Chart
                                    height={"350px"}
                                    options={this.state.splittedChartSummed.options}
                                    series={this.state.splittedChartSummed.series}
                                    type="line"
                                />
                            </div>
                            <div className="mixed-chart col-12 col-lg-6">
                                <Chart
                                    height={"350px"}
                                    options={this.state.splittedChartNotSummed.options}
                                    series={this.state.splittedChartNotSummed.series}
                                    type="line"
                                />
                            </div>
                        </div>
                    </div>
                </Card>
            </div>
        );
    }
}


export default TotalDeathChart;
