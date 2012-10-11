package com.taobao.api.request;

import com.taobao.api.internal.util.RequestCheckUtils;
import java.util.Map;

import com.taobao.api.TaobaoRequest;
import com.taobao.api.internal.util.TaobaoHashMap;
import com.taobao.api.response.JipiaoAgentorderSuccessResponse;
import com.taobao.api.ApiRuleException;
/**
 * TOP API: taobao.jipiao.agentorder.success request
 * 
 * @author auto create
 * @since 1.0, 2012-09-23 16:46:03
 */
public class JipiaoAgentorderSuccessRequest implements TaobaoRequest<JipiaoAgentorderSuccessResponse> {

	private TaobaoHashMap udfParams; // add user-defined text parameters
	private Long timestamp;

	/** 
	* 订单id
	 */
	private Long orderId;

	/** 
	* 成功出票需要的信息。每个元素的结构为：旧乘机人姓名;新乘机人姓名;pnr;票号(以分号进行分隔)。有时用户输入的乘机人姓名输入错误或者有生僻字，代理商必须输入新的名字以保证验真的通过。
	 */
	private String successInfo;

	public void setOrderId(Long orderId) {
		this.orderId = orderId;
	}
	public Long getOrderId() {
		return this.orderId;
	}

	public void setSuccessInfo(String successInfo) {
		this.successInfo = successInfo;
	}
	public String getSuccessInfo() {
		return this.successInfo;
	}

	public Long getTimestamp() {
		return this.timestamp;
	}

	public void setTimestamp(Long timestamp) {
		this.timestamp = timestamp;
	}

	public String getApiMethodName() {
		return "taobao.jipiao.agentorder.success";
	}

	public Map<String, String> getTextParams() {		
		TaobaoHashMap txtParams = new TaobaoHashMap();
		txtParams.put("order_id", this.orderId);
		txtParams.put("success_info", this.successInfo);
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

	public Class<JipiaoAgentorderSuccessResponse> getResponseClass() {
		return JipiaoAgentorderSuccessResponse.class;
	}

	public void check() throws ApiRuleException {
		
		RequestCheckUtils.checkNotEmpty(orderId,"orderId");
		RequestCheckUtils.checkNotEmpty(successInfo,"successInfo");
		RequestCheckUtils.checkMaxListSize(successInfo,9,"successInfo");
	}
}
