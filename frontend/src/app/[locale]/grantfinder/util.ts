import { requesterForEndpoint } from "src/services/fetch/fetchers/fetchers";
import { ApiRequestError, parseErrorStatus } from "src/errors";
import { EndpointConfig } from "src/services/fetch/endpointConfigs";
import { HeadersDict, JSONRequestBody } from "src/services/fetch/fetcherHelpers";


export const callEndpoint = async <ResponseCollection extends {data: unknown[]}>(endpoint: EndpointConfig, _subPath?: string, _body?: JSONRequestBody, _additionalHeaders?: HeadersDict) => {
    let res = {} as ResponseCollection
    try {
        const response = requesterForEndpoint(endpoint)
        const responseBody = ((await response({subPath: _subPath, body: _body, additionalHeaders: _additionalHeaders})).json()) as Promise<ResponseCollection>;
        res = (await responseBody)
    } catch (error) {
        console.error("Failed to render page title due to API error", error);
        if (parseErrorStatus(error as ApiRequestError) === 404) {
          throw error;
        }
    }
    return res

}