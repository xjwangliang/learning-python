package com.taobao.api.request;

import java.util.Map;

import com.taobao.api.TaobaoRequest;
import com.taobao.api.internal.util.TaobaoHashMap;
import com.taobao.api.response.JipiaoAgentordersGetResponse;
import com.taobao.api.ApiRuleException;
/**
 * TOP API: taobao.jipiao.agentorders.get request
 * 
 * @author auto create
 * @since 1.0, 2012-09-23 16:46:03
 */
public class JipiaoAgentordersGetRequest implements TaobaoRequest<JipiaoAgentordersGetResponse> {

	private TaobaoHashMap udfParams; // add user-defined text parameters
	private Long timestamp;

	/** 
	* 1. 未付款的订单
2. 待处理的订单
3. 确认出票的订单
4. 已成功并且需要解冻的订单
	 */
	private String status;

	public void setStatus(String status) {
		this.status = status;
	}
	public String getStatus() {
		return this.status;
	}

	public Long getTimestamp() {
		return this.timestamp;
	}

	public void setTimestamp(Long timestamp) {
		this.timestamp = timestamp;
	}

	public String getApiMethodName() {
		return "taobao.jipiao.agentorders.get";
	}

	public Map<String, String> getTextParams() {		
		TaobaoHashMap txtParams = new TaobaoHashMap();
		txtParams.put("status", this.status);
		if(this.udfParams != null) {
			txtParams.putAll(this.udfParams);
		}
		return txtParams;
	}

	public void putOtherTextParam(String key, String value) {
		if(this.udfParams == null) {
			this.udfParams = new TaobaoHashMap();
		}
		this.udfParams.put(key, value);
	}

	public Class<JipiaoAgentordersGetResponse> getResponseClass() {
		return JipiaoAgentordersGetResponse.class;
	}

	public void check() throws ApiRuleException {
		
	}
}
