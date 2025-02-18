#
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
#
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import deploy_service_pb2 as deploy__service__pb2


class DeployServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.startScheduleWorkflow = channel.unary_unary(
                '/DeployService/startScheduleWorkflow',
                request_serializer=deploy__service__pb2.WorkflowRequest.SerializeToString,
                response_deserializer=deploy__service__pb2.ScheduleResponse.FromString,
                )
        self.stopScheduleWorkflow = channel.unary_unary(
                '/DeployService/stopScheduleWorkflow',
                request_serializer=deploy__service__pb2.WorkflowRequest.SerializeToString,
                response_deserializer=deploy__service__pb2.ScheduleResponse.FromString,
                )
        self.getWorkflowExecutionResult = channel.unary_unary(
                '/DeployService/getWorkflowExecutionResult',
                request_serializer=deploy__service__pb2.WorkflowRequest.SerializeToString,
                response_deserializer=deploy__service__pb2.ScheduleResponse.FromString,
                )
        self.isWorkflowExecutionAlive = channel.unary_unary(
                '/DeployService/isWorkflowExecutionAlive',
                request_serializer=deploy__service__pb2.WorkflowRequest.SerializeToString,
                response_deserializer=deploy__service__pb2.ScheduleResponse.FromString,
                )
        self.getMasterConfig = channel.unary_unary(
                '/DeployService/getMasterConfig',
                request_serializer=deploy__service__pb2.MasterConfigRequest.SerializeToString,
                response_deserializer=deploy__service__pb2.MasterConfigResponse.FromString,
                )


class DeployServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def startScheduleWorkflow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stopScheduleWorkflow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getWorkflowExecutionResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def isWorkflowExecutionAlive(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMasterConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeployServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'startScheduleWorkflow': grpc.unary_unary_rpc_method_handler(
                    servicer.startScheduleWorkflow,
                    request_deserializer=deploy__service__pb2.WorkflowRequest.FromString,
                    response_serializer=deploy__service__pb2.ScheduleResponse.SerializeToString,
            ),
            'stopScheduleWorkflow': grpc.unary_unary_rpc_method_handler(
                    servicer.stopScheduleWorkflow,
                    request_deserializer=deploy__service__pb2.WorkflowRequest.FromString,
                    response_serializer=deploy__service__pb2.ScheduleResponse.SerializeToString,
            ),
            'getWorkflowExecutionResult': grpc.unary_unary_rpc_method_handler(
                    servicer.getWorkflowExecutionResult,
                    request_deserializer=deploy__service__pb2.WorkflowRequest.FromString,
                    response_serializer=deploy__service__pb2.ScheduleResponse.SerializeToString,
            ),
            'isWorkflowExecutionAlive': grpc.unary_unary_rpc_method_handler(
                    servicer.isWorkflowExecutionAlive,
                    request_deserializer=deploy__service__pb2.WorkflowRequest.FromString,
                    response_serializer=deploy__service__pb2.ScheduleResponse.SerializeToString,
            ),
            'getMasterConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.getMasterConfig,
                    request_deserializer=deploy__service__pb2.MasterConfigRequest.FromString,
                    response_serializer=deploy__service__pb2.MasterConfigResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DeployService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DeployService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def startScheduleWorkflow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeployService/startScheduleWorkflow',
            deploy__service__pb2.WorkflowRequest.SerializeToString,
            deploy__service__pb2.ScheduleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def stopScheduleWorkflow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeployService/stopScheduleWorkflow',
            deploy__service__pb2.WorkflowRequest.SerializeToString,
            deploy__service__pb2.ScheduleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getWorkflowExecutionResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeployService/getWorkflowExecutionResult',
            deploy__service__pb2.WorkflowRequest.SerializeToString,
            deploy__service__pb2.ScheduleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def isWorkflowExecutionAlive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeployService/isWorkflowExecutionAlive',
            deploy__service__pb2.WorkflowRequest.SerializeToString,
            deploy__service__pb2.ScheduleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMasterConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeployService/getMasterConfig',
            deploy__service__pb2.MasterConfigRequest.SerializeToString,
            deploy__service__pb2.MasterConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
