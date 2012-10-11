package com.taobao.api.request;

import com.taobao.api.internal.util.RequestCheckUtils;
import java.util.Map;

import com.taobao.api.TaobaoRequest;
import com.taobao.api.internal.util.TaobaoHashMap;
import com.taobao.api.response.JipiaoAgentorderFailResponse;
import com.taobao.api.ApiRuleException;
/**
 * TOP API: taobao.jipiao.agentorder.fail request
 * 
 * @author auto create
 * @since 1.0, 2012-09-23 16:46:03
 */
public class JipiaoAgentorderFailRequest implements TaobaoRequest<JipiaoAgentorderFailResponse> {

	private TaobaoHashMap udfParams; // add user-defined text parameters
	private Long timestamp;

	/** 
	* 备注
	 */
	private String memo;

	/** 
	* 订单id
	 */
	private Long orderId;

	/** 
	* Reason字段为失败原因：分为
1．客户要求失败订单
2．此舱位已售完（经济舱或特舱）
3．剩余座位少于用户购买数量
4．特价管理里录入的特价票已经售完
5．假舱（请及时通过旺旺或者电话反馈给淘宝工作人员）
0．其它（请在备注中说明原因）
	 */
	private Long reason;

	public void setMemo(String memo) {
		this.memo = memo;
	}
	public String getMemo() {
		return this.memo;
	}

	public void setOrderId(Long orderId) {
		this.orderId = orderId;
	}
	public Long getOrderId() {
		return this.orderId;
	}

	public void setReason(Long reason) {
		this.reason = reason;
	}
	public Long getReason() {
		return this.reason;
	}

	public Long getTimestamp() {
		return this.timestamp;
	}

	public void setTimestamp(Long timestamp) {
		this.timestamp = timestamp;
	}

	public String getApiMethodName() {
		return "taobao.jipiao.agentorder.fail";
	}

	public Map<String, String> getTextParams() {		
		TaobaoHashMap txtParams = new TaobaoHashMap();
		txtParams.put("memo", this.memo);
		txtParams.put("order_id", this.orderId);
		txtParams.put("reason", this.reason);
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

	public Class<JipiaoAgentorderFailResponse> getResponseClass() {
		return JipiaoAgentorderFailResponse.class;
	}

	public void check() throws ApiRuleException {
		
		RequestCheckUtils.checkMaxLength(memo,100,"memo");
		RequestCheckUtils.checkNotEmpty(orderId,"orderId");
		RequestCheckUtils.checkNotEmpty(reason,"reason");
		RequestCheckUtils.checkMaxValue(reason,5L,"reason");
		RequestCheckUtils.checkMinValue(reason,0L,"reason");
	}
}
