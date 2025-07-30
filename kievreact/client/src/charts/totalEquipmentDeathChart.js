import React, { Component } from "react";
import Chart from "react-apexcharts";
import '../App.css';
import { Card, InputNumber, Button, Space, message } from 'antd';
import { chartService } from '../services/chart.service'
import { chartOption } from '../utils/chart.option'

const default_days = 7
const importedOptions = chartOption.getHeatMapChart()

class TotalEquipmentDeathChart extends Component {
    constructor(props) {
        super(props);
        this.state = {
            equipmentChart : {
                options: {
                    ...importedOptions,
                },
                series : []
            },
            deathChart : {
                options: {
                    ...importedOptions
                },
                series : []
            },
            days : default_days
        };
    }

    componentDidMount() {
        this.getDeathEquipmentChart(default_days);
    }

    setDays(days) {
        if(days !== undefined){
            this.setState({
                days: days
            });
            this.getDeathEquipmentChart( days);
        }
        
    }

    getDeathEquipmentChart = (days) => {
        chartService.getDeathEquipment(days).then(res => {
            
            this.setState({
                equipmentChart : {
                    options: {
                        xaxis: res['equipment']["xaxis"]
                    },
                    series: res['equipment']["series"]
                },
                deathChart : {
                    options: {
                        xaxis: res['human']["xaxis"]
                    },
                    series: res['human']["series"]
                }
            });
           
        },
        error=>{
          console.log('ERROR',error)
          message.error(`An error occurred during getting total equipment death chart`);
        });
    }

    render() {
        return (
            <div className="site-card-border-less-wrapper">
                <Card title="Vehicles Destroyed And Death Chart" className="mt-5" bordered={false} extra={
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
                                    options={this.state.equipmentChart.options}
                                    series={this.state.equipmentChart.series}
                                    height={"350px"}
                                    type="heatmap"
                                />
                            </div>
                            <div className="mixed-chart col-12 col-lg-6">
                                <Chart
                                    options={this.state.deathChart.options}
                                    series={this.state.deathChart.series}
                                    height={"350px"}
                                    type="heatmap"
                                />
                                
                            </div>
                        </div>
                    </div>
                </Card>
            </div>
        );
    }
}


export default TotalEquipmentDeathChart;
