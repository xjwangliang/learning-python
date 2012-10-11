package com.taobao.api.request;

import java.util.Date;
import com.taobao.api.internal.util.RequestCheckUtils;
import java.util.Map;

import com.taobao.api.TaobaoRequest;
import com.taobao.api.internal.util.TaobaoHashMap;
import com.taobao.api.response.JipiaoAgentorderConfirmResponse;
import com.taobao.api.ApiRuleException;
/**
 * TOP API: taobao.jipiao.agentorder.confirm request
 * 
 * @author auto create
 * @since 1.0, 2012-09-23 16:46:03
 */
public class JipiaoAgentorderConfirmRequest implements TaobaoRequest<JipiaoAgentorderConfirmResponse> {

	private TaobaoHashMap udfParams; // add user-defined text parameters
	private Long timestamp;

	/** 
	* 最迟出票时间
	 */
	private Date latestTicketTime;

	/** 
	* 订单id
	 */
	private Long orderId;

	public void setLatestTicketTime(Date latestTicketTime) {
		this.latestTicketTime = latestTicketTime;
	}
	public Date getLatestTicketTime() {
		return this.latestTicketTime;
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
		return "taobao.jipiao.agentorder.confirm";
	}

	public Map<String, String> getTextParams() {		
		TaobaoHashMap txtParams = new TaobaoHashMap();
		txtParams.put("latest_ticket_time", this.latestTicketTime);
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

	public Class<JipiaoAgentorderConfirmResponse> getResponseClass() {
		return JipiaoAgentorderConfirmResponse.class;
	}

	public void check() throws ApiRuleException {
		
		RequestCheckUtils.checkNotEmpty(latestTicketTime,"latestTicketTime");
		RequestCheckUtils.checkNotEmpty(orderId,"orderId");
	}
}
