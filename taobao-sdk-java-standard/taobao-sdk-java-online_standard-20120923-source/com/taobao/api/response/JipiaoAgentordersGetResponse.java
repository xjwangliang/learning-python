package com.taobao.api.response;

import java.util.List;
import com.taobao.api.internal.mapping.ApiField;
import com.taobao.api.internal.mapping.ApiListField;
import com.taobao.api.domain.EtOrder;

import com.taobao.api.TaobaoResponse;

/**
 * TOP API: taobao.jipiao.agentorders.get response.
 * 
 * @author auto create
 * @since 1.0, null
 */
public class JipiaoAgentordersGetResponse extends TaobaoResponse {

	private static final long serialVersionUID = 5667214122973995441L;

	/** 
	 * 订单列表
	 */
	@ApiListField("orders")
	@ApiField("et_order")
	private List<EtOrder> orders;

	public void setOrders(List<EtOrder> orders) {
		this.orders = orders;
	}
	public List<EtOrder> getOrders( ) {
		return this.orders;
	}

}
