# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from airflow.models.dag import DAG
from airflow.utils import timezone
from airflow.contrib.jobs.event_handlers import AIFlowHandler
from airflow.operators.bash import BashOperator

dag = DAG(dag_id='workflow_1', start_date=timezone.utcnow(), schedule_interval='@once')
op_0 = BashOperator(task_id='0_job', dag=dag, bash_command='echo "0 hello word!"')
op_1 = BashOperator(task_id='1_job', dag=dag, bash_command='echo "1 hello word!"')
op_2 = BashOperator(task_id='2_job', dag=dag, bash_command='echo "2 hello word!"')
op_1.subscribe_event('key_1', 'UNDEFINED', 'default')
configs_op_1='[{"__af_object_type__": "jsonable", "__class__": "MetConfig", "__module__": "ai_flow.graph.edge", "action": "START", "condition": "NECESSARY", "event_key": "key_1", "event_type": "UNDEFINED", "event_value": "value_1", "life": "ONCE", "namespace": "default", "value_condition": "EQUAL"}]'

op_1.set_events_handler(AIFlowHandler(configs_op_1))
op_2.subscribe_event('key_2', 'UNDEFINED', 'default')
configs_op_2='[{"__af_object_type__": "jsonable", "__class__": "MetConfig", "__module__": "ai_flow.graph.edge", "action": "START", "condition": "NECESSARY", "event_key": "key_2", "event_type": "UNDEFINED", "event_value": "value_2", "life": "ONCE", "namespace": "default", "value_condition": "EQUAL"}]'

op_2.set_events_handler(AIFlowHandler(configs_op_2))
