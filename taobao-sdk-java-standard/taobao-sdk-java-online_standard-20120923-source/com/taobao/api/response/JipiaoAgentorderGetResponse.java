package com.taobao.api.response;

import com.taobao.api.internal.mapping.ApiField;
import com.taobao.api.domain.EtOrder;

import com.taobao.api.TaobaoResponse;

/**
 * TOP API: taobao.jipiao.agentorder.get response.
 * 
 * @author auto create
 * @since 1.0, null
 */
public class JipiaoAgentorderGetResponse extends TaobaoResponse {

	private static final long serialVersionUID = 8532354865855172471L;

	/** 
	 * 订单信息
	 */
	@ApiField("order")
	private EtOrder order;

	public void setOrder(EtOrder order) {
		this.order = order;
	}
	public EtOrder getOrder( ) {
		return this.order;
	}

}
