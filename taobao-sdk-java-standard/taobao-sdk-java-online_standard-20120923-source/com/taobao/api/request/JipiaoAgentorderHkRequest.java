package com.taobao.api.request;

import com.taobao.api.internal.util.RequestCheckUtils;
import java.util.Map;

import com.taobao.api.TaobaoRequest;
import com.taobao.api.internal.util.TaobaoHashMap;
import com.taobao.api.response.JipiaoAgentorderHkResponse;
import com.taobao.api.ApiRuleException;
/**
 * TOP API: taobao.jipiao.agentorder.hk request
 * 
 * @author auto create
 * @since 1.0, 2012-09-23 16:46:03
 */
public class JipiaoAgentorderHkRequest implements TaobaoRequest<JipiaoAgentorderHkResponse> {

	private TaobaoHashMap udfParams; // add user-defined text parameters
	private Long timestamp;

	/** 
	* hk（占座）时需要的信息，这是一个list，list中的每个元素的结构为:“乘机人姓名;pnr”(以分号进行分隔).
	 */
	private String hkInfo;

	/** 
	* 订单id
	 */
	private Long orderId;

	public void setHkInfo(String hkInfo) {
		this.hkInfo = hkInfo;
	}
	public String getHkInfo() {
		return this.hkInfo;
	}

	public void setOrderId(Long orderId) {
		this.orderId = orderId;
	}
	public Long getOrderId() {
		return this.orderId;
	}

	public Long getTimestamp() {
		return this.timestamp;
	}

	public void setTimestamp(Long timestamp) {
		this.timestamp = timestamp;
	}

	public String getApiMethodName() {
		return "taobao.jipiao.agentorder.hk";
	}

	public Map<String, String> getTextParams() {		
		TaobaoHashMap txtParams = new TaobaoHashMap();
		txtParams.put("hk_info", this.hkInfo);
		txtParams.put("order_id", this.orderId);
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

	public Class<JipiaoAgentorderHkResponse> getResponseClass() {
		return JipiaoAgentorderHkResponse.class;
	}

	public void check() throws ApiRuleException {
		
		RequestCheckUtils.checkNotEmpty(hkInfo,"hkInfo");
		RequestCheckUtils.checkMaxListSize(hkInfo,9,"hkInfo");
		RequestCheckUtils.checkNotEmpty(orderId,"orderId");
	}
}
