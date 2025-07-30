import React, { Component } from "react";
import Chart from "react-apexcharts";
import '../App.css';
import { Card, InputNumber, Button, Space, message } from 'antd';
import { chartService } from '../services/chart.service'
import { chartOption } from '../utils/chart.option'

const default_days = 19
const importedOptions = chartOption.getSplittedChart();

class TotalEquipmentChart extends Component {
    constructor(props) {
        super(props);
        this.state = {
            totalChartSummed : {
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
            days : default_days
        };
    }

    componentDidMount() {
        this.getEquipmentChart(default_days, "sum");
        this.getEquipmentChart(default_days, "sub");
    }

    setDays(days) {
        if(days !== undefined){
            this.setState({
                days: days
            });
            this.getEquipmentChart( days, "sum");
            this.getEquipmentChart( days, "sub");
        }
    }

    getEquipmentChart = (days, sumType) => {
        chartService.getTotalEquipment( days, sumType ).then(res => {
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
        },
        error=>{
          console.log('ERROR',error)
          message.error(`An error occurred during getting total equipment chart`);
        });
    }

    render() {
        return (
            <div className="site-card-border-less-wrapper">
                <Card title="Total Vehicles Destroyed Chart" className="mt-5" bordered={false} extra={
                    <Space>
                        <InputNumber min={1} max={99} value={this.state.days} onChange={(e) => this.setDays(e)} />
                        <Button type="primary" onClick={() => { this.setDays(default_days); }}>
                            Reset
                        </Button>
                    </Space>
                }>
                    <div className="app">
                        <div className="row">
                            <div className="mixed-chart col-12 col-lg-6 ">
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
                    </div>
                </Card>
            </div>
        );
    }
}


export default TotalEquipmentChart;
